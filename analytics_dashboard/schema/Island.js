cube(`Island`, {
  sql: `SELECT * FROM threekeco.island`,
  
  preAggregations: {
    // Pre-Aggregations definitions go here
    // Learn more here: https://cube.dev/docs/caching/pre-aggregations/getting-started  
  },
  
  joins: {

  },
  
  measures: {
    count: {
      type: `count`,
    }
  },
  
  dimensions: {
    id: {
      sql: `id`,
      type: `number`,
      primaryKey: true
    },
    name: {
      sql: `name`,
      type: `string`
    },
  },
  
  dataSource: `default`
});
