<script lang="ts">
  // Layout components
  import Cell from "$lib/layouts/Cell.svelte";
  import CenterBanner from "$lib/layouts/CenterBanner.svelte";
  import Grid from "$lib/layouts/Grid.svelte";
  import Divider from "$lib/layouts/Divider.svelte";

  // Stateful components
  import ChronChart from "$lib/components/ChronChart.svelte";
  import ScalarStats from "$lib/components/ScalarStats.svelte";

  // Types
  import type { Query } from "@cubejs-client/core";
  import PieChart from "$lib/components/PieChart.svelte";
  import ColorChooser from "$lib/components/ColorChooser.svelte";
  import { dev } from "$app/env";

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

{#if dev}
  <ColorChooser />
{/if}

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
    <ChronChart query={exampleQuery} />
  </Cell>
  <Cell>
    <PieChart
      query={{
        measures: ["infrared_sensor.activations"],
        timeDimensions: [],
        order: { "infrared_sensor.activations": "desc" },
        filters: [],
        dimensions: ["Bin.category"],
      }}
    />
  </Cell>
</Grid>
