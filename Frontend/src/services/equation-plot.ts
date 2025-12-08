import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class EquationPlot {

  private equationSource = new BehaviorSubject<string>('');
  equation$ = this.equationSource.asObservable();

  setEquation(equation: string) {
    this.equationSource.next(equation);
  }
  
}
