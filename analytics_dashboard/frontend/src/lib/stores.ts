import cubejs from "@cubejs-client/core";
import { readable } from "svelte/store";

export let cubeClient = readable(
    cubejs('token', {
        apiUrl: 'http://localhost:4000/cubejs-api/v1'
    })
)
