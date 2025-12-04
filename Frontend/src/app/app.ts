import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './app.html',
  styleUrls: ['./app.css']
})

export class App {
  protected readonly title = signal('Frontend');

  // Text inputs
  method: string = '';
  functionInput: string = '';
  gx: string = 'x';
  precision: number = 17;
  tolerance: number = 0.00001;
  maxIterations: number = 50;
  fromInput: number = 0;
  toInput: number = 1;
  intialGuess: number = 0;
  intialGuess2: number = 0;
  showSteps: boolean = false;

  // Answer from backend
  response :any = null;

  constructor(private http: HttpClient){}


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
    const steps = this.showSteps;

    console.log(func);
    console.log(tol);
    console.log(from_value);
    console.log(to_value);
    console.log(method);
    console.log(precision);
    console.log(maxIterations);
    console.log(intialGuess);
    console.log(intialGuess2);
    console.log(gx);
    console.log(steps);


    const apiURL = 'http://127.0.0.1:8000';

    if(this.method == 'bisection' || this.method == 'false position'){

      const bracketing = {
        method,
        func,
        from_value,
        to_value,
        precision,
        tol,
        maxIterations,
        steps
      };

      this.http.post(`${apiURL}/bracketing`, bracketing).subscribe({
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
        maxIterations,
        steps
      };

      this.http.post(`${apiURL}/newton`, newton).subscribe({
        next: (res: any) => {
          this.response = res;
          console.log('Backend result:', res);
        },
        error: (err: any) => console.error('Error:', err)
      })
    }
    else if(this.method == 'fixed point'){

      const fixed = {
        func,
        gx,
        intialGuess,
        precision,
        tol,
        maxIterations,
        steps
      };

      this.http.post(`${apiURL}/fixed`, fixed).subscribe({
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
        maxIterations,
        steps
      };

      this.http.post(`${apiURL}/secant`, secant).subscribe({
        next: (res: any) => {
          this.response = res;
          console.log('Backend result:', res);
        },
        error: (err: any) => console.error('Error:', err)
      })
    }
  }
}