import type { CubejsApi, Query, ResultSet } from "@cubejs-client/core";
import type { ChartData } from "chart.js";

// TODO: Get evenly spaced colors
function randomColor() {
  return "#" + ((Math.random() * 0xffffff) << 0).toString(16);
}

export const cubeDataToLineData = (
  cubeData: ResultSet,
  colors?: string | string[]
): ChartData => {
  const series = cubeData.series();

  const data: ChartData = {
    labels: series[0].series.map((entry) => entry.x), // All datasets should have the same values as x
    datasets: series.map((s, i) => {
      const color: string =
        colors == undefined ? randomColor() : colors[i] || randomColor();

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
