import type { CubejsApi, Query, ResultSet } from "@cubejs-client/core";
import cubejs from "@cubejs-client/core";
import { readable } from "svelte/store";
import { apiPath, apiToken } from "./variables";

// TODO: persistence with LocalStorage

class AnyCache<K, T> {
  // Composition rather than inheritance, to model the types better
  private _map: Map<string, T>;

  constructor() {
    this._map = new Map();
  }

  public get size(): Number {
    return this._map.size;
  }

  has(key: K): boolean {
    return this._map.has(JSON.stringify(key));
  }

  get(key: K): T {
    return this._map.get(JSON.stringify(key));
  }

  set(key: K, value: T) {
    this._map.set(JSON.stringify(key), value);
  }
}

let cubeClient = cubejs(apiToken, {
  apiUrl: apiPath,
});

const queryCache: AnyCache<Query, Promise<ResultSet>> = new AnyCache();

const id = Math.random();

export const cachedCubeLoad = (query: Query): Promise<ResultSet> => {
  if (queryCache.has(query)) {
    // console.debug("Cache hit", queryCache.size);
    return queryCache.get(query);
  }
  // console.debug(
  //   `Cache miss, making request, chache size ${queryCache.size}, id: ${id}`
  // );
  const r = cubeClient.load(query);
  queryCache.set(query, r);
  return r;
};
