<script lang="ts">
  import ChronChart from "$lib/components/ChronChart.svelte";
  import Cell from "$lib/layouts/Cell.svelte";
  import CenterBanner from "$lib/layouts/CenterBanner.svelte";
  import Grid from "$lib/layouts/Grid.svelte";
  import ScalarStats from "$lib/components/ScalarStats.svelte";
  import type { Query } from "@cubejs-client/core";
  import Container from "$lib/layouts/Container.svelte";
  import Divider from "$lib/layouts/Divider.svelte";

  const exampleQuery: Query = {
    measures: ["infrared_sensor.activations"],
    timeDimensions: [
      {
        dimension: "infrared_sensor.measuredOn",
        granularity: "day",
      },
    ],
    filters: [],
    dimensions: ["Bin.category"],
  };
</script>

<h1 class="text-2xl font-medium mt-4">This is the homepage</h1>

<CenterBanner>
  <ScalarStats
    queries={[
      {
        title: "Number of bins",
        query: { measures: ["Bin.count"] },
      },
      {
        title: "Number of islands",
        query: { measures: ["Island.count"] },
      },
    ]}
  />
</CenterBanner>

<Divider />

<Grid>
  <Cell>
    <ChronChart query={exampleQuery} colors={undefined} />
  </Cell>
  <Cell>
    <ChronChart query={exampleQuery} colors={undefined} />
  </Cell>
  <Cell>
    <ChronChart query={exampleQuery} colors={undefined} />
  </Cell>
  <Cell>
    <ChronChart query={exampleQuery} colors={undefined} />
  </Cell>
  <Cell>
    <ChronChart query={exampleQuery} colors={undefined} />
  </Cell>
</Grid>
