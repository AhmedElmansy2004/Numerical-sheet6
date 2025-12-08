import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PlotlyChart } from './plotly-chart';

describe('PlotlyChart', () => {
  let component: PlotlyChart;
  let fixture: ComponentFixture<PlotlyChart>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PlotlyChart]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PlotlyChart);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
