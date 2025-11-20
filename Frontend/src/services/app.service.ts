import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface PolynomialTerm {
  coefficient: number;
  exponent: number;
}

@Injectable({
  providedIn: 'root'
})
export class AppService {
  private apiUrl = 'http://localhost:3000/calculate'; // replace with your backend URL

  constructor(private http: HttpClient) {}

  // Send polynomial data to backend
  calculatePolynomial(
    terms: PolynomialTerm[],
    tolerance: number,
    from: number,
    to: number,
    method: string,
    errorType: string
  ): Observable<any> {
    const payload = {
      terms,
      tolerance,
      from,
      to,
      method,
      errorType
    };
    return this.http.post(this.apiUrl, payload);
  }
}
