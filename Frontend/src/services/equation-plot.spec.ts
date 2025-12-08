import { TestBed } from '@angular/core/testing';

import { EquationPlot } from './equation-plot';

describe('EquationPlot', () => {
  let service: EquationPlot;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EquationPlot);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
