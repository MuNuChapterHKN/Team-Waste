<script lang="ts">
  import type { ScalarQuery } from "../../types/scalar_query.type";
  import { cachedCubeLoad } from "$lib/utils/cachingCubeClient";

  export let queries: Array<ScalarQuery>;

  let getResults = async () =>
    Promise.all(
      queries.map(async (q) => {
        return {
          title: q.title,
          value: (await cachedCubeLoad(q.query)).series()[0].series[0].value, // The series contains just one value
        };
      })
    );
</script>

{#await getResults()}
  <div class="btn loading m-8">Loading</div>
{:then list}
  <div class="stats shadow">
    {#each list as metric}
      <div class="stat text-center">
        <div class="stat-title">{metric.title}</div>
        <div class="stat-value">{metric.value}</div>
      </div>
    {/each}
  </div>
{:catch}
  <div class="btn btn-error m-8">Loading error</div>
{/await}
