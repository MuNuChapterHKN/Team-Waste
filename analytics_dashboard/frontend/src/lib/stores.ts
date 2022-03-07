import cubejs, { movePivotItem, ResultSet } from "@cubejs-client/core";
import { readable, writable } from "svelte/store";

export let cubeClient = readable(
  // TODO: decide If this store is actually needed:
  //       is user authentication part of this web app?
  cubejs("token", {
    apiUrl: "http://localhost:4000/cubejs-api/v1",
  })
);
