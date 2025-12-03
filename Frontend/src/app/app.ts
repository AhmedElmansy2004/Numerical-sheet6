import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, FormsModule],
  templateUrl: './app.html',
  styleUrls: ['./app.css']
})

export class App {
  protected readonly title = signal('Frontend');

  // Text inputs
  method: string = '';
  functionInput: string = '';
  gx: string = '';
  precision: number = 17;
  tolerance: number = 0.00001;
  maxIterations: number = 50;
  fromInput: number = 0;
  toInput: number = 1;
  intialGuess: number = 0;
  intialGuess2: number = 0;

  // Answer from backend
  response :any = null;

  

  constructor(private http: HttpClient){}

  /*parseFunction(func: string){
    func = func.toLowerCase();
    func = func.replace(/\s+/g, '');

    const funcList = func.match(/([+-]?[^+-]+)/g);

    if (!funcList) return [];

    const terms: PolynomialTerm[]  = funcList.map(term => {
      let sign = 1;
      if (term[0] === '-') {
        sign = -1;
        term = term.substring(1);
      } else if (term[0] === '+') {
        term = term.substring(1);
      }

      let coefficient = 0;
      let exponent = 0;

      if(term.includes('x')){
        const [coefPart, expPart] = term.split('x^');

        if(coefPart.includes('/'))
          coefficient = (parseFloat(coefPart[0]) / parseFloat(coefPart[2])) * sign;
        else
          coefficient = ((coefPart === '')? 1: parseFloat(coefPart)) * sign;

        if(expPart === undefined)
          exponent = 1
        else{
          if(expPart.includes('/'))
            exponent = (parseFloat(expPart[0]) / parseFloat(expPart[2]));
          else
            exponent = parseFloat(expPart);
        }

        
      }
      else {
        coefficient = parseFloat(term) * sign;
        exponent = 0;
      }

      return {coefficient, exponent};
    });

    return terms;
  }*/

  // Submit function
  calculate() {

    const func = this.functionInput;
    const tol = this.tolerance;
    const from_value = this.fromInput;
    const to_value = this.toInput;
    const method = this.method;
    const precision = this.precision;
    const maxIterations = this.maxIterations;
    const intialGuess = this.intialGuess;
    const intialGuess2 = this.intialGuess2;
    const gx = this.gx;

    const apiURL = 'http://127.0.0.1:8000/bracketing';

    if(this.method == 'bisection' || this.method == 'false position'){

      const bracketing = {
        method,
        func,
        from_value,
        to_value,
        precision,
        tol,
        maxIterations
      };

      this.http.post('${apiURL}/bracketing', bracketing).subscribe({
        next: (res: any) => {
          this.response = res;
          console.log('Backend result:', res);
        },
        error: (err: any) => console.error('Error:', err)
      })
    }
    else if(this.method == 'orginal newton' || this.method == 'modified newton'){

      const newton = {
        method,
        func,
        intialGuess,
        precision,
        tol,
        maxIterations
      };

      this.http.post('${apiURL}/newton', newton).subscribe({
        next: (res: any) => {
          this.response = res;
          console.log('Backend result:', res);
        },
        error: (err: any) => console.error('Error:', err)
      })
    }
    else if(this.method == 'fixed'){

      const fixed = {
        func,
        gx,
        intialGuess,
        precision,
        tol,
        maxIterations
      };

      this.http.post('${apiURL}/fixed', fixed).subscribe({
        next: (res: any) => {
          this.response = res;
          console.log('Backend result:', res);
        },
        error: (err: any) => console.error('Error:', err)
      })
    }
    else if(this.method == 'secant'){

      const secant = {
        func,
        intialGuess,
        intialGuess2,
        precision,
        tol,
        maxIterations
      };

      this.http.post('${apiURL}/secant', secant).subscribe({
        next: (res: any) => {
          this.response = res;
          console.log('Backend result:', res);
        },
        error: (err: any) => console.error('Error:', err)
      })
    }
  }
}