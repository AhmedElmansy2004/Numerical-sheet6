import { Component, OnInit, ElementRef } from '@angular/core';
import Plotly from 'plotly.js-dist-min';
import { evaluate } from 'mathjs';
import { EquationPlot } from '../../services/equation-plot';

@Component({
  selector: 'app-plotly-chart',
  templateUrl: './plotly-chart.html',
  styleUrl: './plotly-chart.css',
})
export class PlotlyChart implements OnInit {
  equation: string = '';
  step: number = 0.1; // smaller step for smoother curve

  constructor(private el: ElementRef, private equationPlot: EquationPlot) {}

  ngOnInit() {
    // Subscribe to equation changes
    this.equationPlot.equation$.subscribe((eq) => {
      this.equation = eq;
      this.initializePlot();
    });
  }

  // Initial empty plot
  initializePlot() {
    const chartDiv = this.el.nativeElement.querySelector('#chart');

    const layout = {
      title: { text: this.equation },
      xaxis: { title: { text: 'x' }, autorange: true, fixedrange: false },
      yaxis: { title: { text: 'y' }, autorange: true, fixedrange: false },
      dragmode: 'pan' as 'pan',
    };

    const config = { scrollZoom: true };

    Plotly.newPlot(
      chartDiv,
      [
        {
          x: [],
          y: [],
          type: 'scatter',
          mode: 'lines',
          line: { width: 3 },
        },
      ],
      layout,
      config
    );

    // Listen for pan/zoom events
    chartDiv.on('plotly_relayout', (event: any) => {
      this.updateVisibleRange(event);
    });

    // Draw initial visible range
    this.updateVisibleRange({});
  }

  // Update the function points according to current visible range
  updateVisibleRange(event: any) {
    const chartDiv = this.el.nativeElement.querySelector('#chart');

    // Get current x-axis range from the event or from layout
    let xStart: number, xEnd: number;

    if (event['xaxis.range[0]'] !== undefined && event['xaxis.range[1]'] !== undefined) {
      xStart = event['xaxis.range[0]'];
      xEnd = event['xaxis.range[1]'];
    } else if (chartDiv.layout?.xaxis?.range) {
      [xStart, xEnd] = chartDiv.layout.xaxis.range;
    } else {
      // Default initial range
      xStart = -10;
      xEnd = 10;
    }

    const x: number[] = [];
    const y: number[] = [];

    for (let i = xStart; i <= xEnd; i += this.step) {
      x.push(i);
      let result = NaN;
      try {
        result = evaluate(this.equation, { x: i });
      } catch (e) {}
      y.push(result);
    }

    Plotly.react(
      chartDiv,
      [{ x, y, type: 'scatter', mode: 'lines', line: { width: 3 } }],
      chartDiv.layout,
      { scrollZoom: true }
    );
  }
}
