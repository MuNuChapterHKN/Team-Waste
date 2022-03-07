import cubejs, { movePivotItem, ResultSet } from "@cubejs-client/core";
import { readable, writable } from "svelte/store";

export let cubeClient = readable(
    cubejs('token', {
        apiUrl: 'http://localhost:4000/cubejs-api/v1'
    })
)