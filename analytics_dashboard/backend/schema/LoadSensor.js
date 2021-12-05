cube(`LoadSensor`, {
  sql: `SELECT * FROM load_sensor`,

  measures: {
    averageWeight: {
      type: `avg`,
      sql: `${netWeight}`
    },
    minWeight: {
      type: `min`,
      sql: `${netWeight}`
    }
  },

  joins: {
    Bin: {
      relationship: `belongsTo`,
      sql: `${CUBE}.bin_id = ${Bin}.id`
    }
  },

  dimensions: {
    id: {
      sql: `id`,
      type: `number`,
      primaryKey: true
    },
    netWeight: {
      sql: `value`,
      type: `number`,
      description: `Net weight of waste in the bin`
    },
    measuredOn: {
      sql: `measured_on`,
      type: `time`
    }
  }
})