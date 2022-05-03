import type { CubejsApi, Query, ResultSet } from "@cubejs-client/core";
import type { ChartData } from "chart.js";

// TODO: Get evenly spaced colors
function randomColor() {
  return "#" + ((Math.random() * 0xffffff) << 0).toString(16);
}

// TODO: handle case of empty response (there is no data for the range specified)
export const cubeDataToLineData = (
  cubeData: ResultSet,
  colors?: string | string[]
): ChartData => {
  const series = cubeData.series();
  const n = series[0].series.length;

  const data: ChartData = {
    labels: series[0].series.map((entry) => entry.x), // All datasets should have the same values as x
    datasets: series.map((s, i) => {
      const color: string =
        colors == undefined ? randomColor() : colors[i%n];

      return {
        label: s.title.split(",")[0],
        borderColor: color,
        backgroundColor: color,
        data: s.series.map((e) => e.value),
      };
    }),
  };

  return data;
};

// TODO: Proper support for colors
export const cubeDataToPieData = (
  cubeData: ResultSet,
  colors?: string | string[]
): ChartData => {
  const series = cubeData.series();

  const s = series[0].series;
  const n = s.length;
  const backgrounds: string[] = [];
  for (let i=0; i<n; i++) {
    backgrounds[i] = colors === undefined ? randomColor() : colors[i%n];
  }

  return {
    labels: s.map(e => e.x),
    datasets: [{
      label: series[0].key,
      data: s.map(e => e.value),
      backgroundColor: backgrounds
    }]
  }
}