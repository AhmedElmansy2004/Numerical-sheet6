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
  functionInput: string = '';
  precision: number = 17;
  tolerance: number = 8;
  maxIterations: number = 50;
  fromInput: string = '';
  toInput: string = '';

  result: number | null = null;

  method: string = '';

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

    const method = (this.method === 'bisection')? 'bt': 'fp';

    const tol = this.tolerance;
    const from = parseFloat(this.fromInput);
    const to = parseFloat(this.toInput);

    const func = this.functionInput;

    const payload = {
      func,
      tol,
      from,
      to,
      method,
    };

    this.http.post('http://127.0.0.1:8000/calculate', payload).subscribe({
      next: (res: any) => {
        this.result = res.root;
        console.log('Backend result:', res);
      },
      error: (err: any) => console.error('Error:', err)
    })
  }
}
