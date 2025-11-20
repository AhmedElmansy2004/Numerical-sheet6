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
  private apiUrl = 'http://127.0.0.1:8000';

  constructor(private http: HttpClient) {}

  // Send polynomial data to backend
  calculatePolynomial(
    terms: PolynomialTerm[],
    tolerance: number,
    from_value: number,
    to_value: number,
    method: string,
    errorType: string
  ): Observable<any> {
    const payload = {
      terms,
      tolerance,
      from_value,
      to_value,
      method,
      errorType
    };
    return this.http.post(`${this.apiUrl}/calculate`, payload);
  }
}
