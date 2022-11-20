import React from "react";
import {XYPlot, XAxis, YAxis, LineChart} from 'reactochart';
import 'reactochart/styles.css';


 // Sample data

 const lineChartData = {
    labels: ["October", "November", "December"],
    datasets: [
      {
        data: [8137119, 9431691, 10266674],
        label: "Infected",
        borderColor: "#3333ff",
        fill: true,
        lineTension: 0.5
      },
      {
        data: [1216410, 1371390, 1477380],
        label: "Deaths",
        borderColor: "#ff3333",
        backgroundColor: "rgba(255, 0, 0, 0.5)",
        fill: true,
        lineTension: 0.5
      }
    ]
  };

const Linechart = () => {
  return (
    <div className="linechart">
        <XYPlot>
        <XAxis title="Phase" />
        <YAxis title="Intensity" />
        <LineChart
        data={Array(100)
            .fill()
            .map((e, i) => i + 1)}
        x={d => d}
        y={d => Math.sin(d * 0.1)}
        />
  </XYPlot>
    </div>
  );
};

export default Linechart;