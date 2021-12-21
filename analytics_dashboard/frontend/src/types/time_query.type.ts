import type { Query } from "@cubejs-client/core";

export type TimeQuery = {
    query: Query,
    colors?: string[],
    colorScheme?: string
}