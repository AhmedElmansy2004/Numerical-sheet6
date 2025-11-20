import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { AppService, PolynomialTerm } from '../services/app.service';

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
  toleranceInput: string = '';
  fromInput: string = '';
  toInput: string = '';

  // Radio selections
  selectedMethod: string = 'bisection';
  selectedErrorType: string = 'absolute';

  constructor(private appservice: AppService){}

  parseFunction(func: string){
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

        coefficient = ((coefPart === '')? 1: parseFloat(coefPart)) * sign;
        exponent = (expPart === undefined)? 1: parseFloat(expPart);
      }
      else {
        coefficient = parseFloat(term) * sign;
        exponent = 0;
      }

      return {coefficient, exponent};
    });

    return terms;
  }

  // Submit function
  calculate() {
    console.log('Function:', this.functionInput);
    console.log('Tolerance:', this.toleranceInput);
    console.log('From:', this.fromInput);
    console.log('To:', this.toInput);
    console.log('Method:', this.selectedMethod);
    console.log('Error Type:', this.selectedErrorType);

    const polynomial = this.parseFunction(this.functionInput);

    console.log(polynomial)

    const tol = parseFloat(this.toleranceInput);
    const from = parseFloat(this.fromInput);
    const to = parseFloat(this.toInput);

    this.appservice.calculatePolynomial(polynomial, tol, from, to, this.selectedMethod, this.selectedErrorType).subscribe({
      next: res => console.log('Backend result:', res),
      error: err => console.error('Error:', err)
    })
  }


}
