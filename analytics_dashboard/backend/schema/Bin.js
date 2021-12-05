cube(`Bin`, {
  sql: `select * from threekeco.bin`,

  measures: {
    count: {
      type: `count`
    }
  },

  joins: {
    Island: {
      relationship: `belongsTo`,
      sql: `${CUBE}.island_id = ${Island}.id`
    }
  },

  dimensions: {
    id: {
      sql: `id`,
      type: `number`,
      primaryKey: true
    },
    category: {
      type: `string`,
      description: `Kind of garbage`,
      case: {
        when: [
          { sql: `${CUBE}.type = 1`, label: `glass and cans` },
          { sql: `${CUBE}.type = 2`, label: `compostable` },
          { sql: `${CUBE}.type = 3`, label: `paper` },
          { sql: `${CUBE}.type = 4`, label: `plastic` },
          { sql: `${CUBE}.type = 5`, label: `waste` },
        ]
      }
    }
  }
})