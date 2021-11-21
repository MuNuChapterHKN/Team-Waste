cube(`infrared_sensor`, {
  sql: `select * from threekeco.infrared_sensor`,

  measures: {
    activations: {
      type: `count`,
      description: `Number of items thrown in the bin`
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
    measuredOn: {
      sql: `measured_on`,
      type: `time`
    }
  }
})