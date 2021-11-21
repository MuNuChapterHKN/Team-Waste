cube(`VolumeSensor`, {
  sql: `SELECT * FROM volume_sensor`,

  measures: {
    average: {
      sql: `${volumePercentage}`,
      type: `avg`
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
    volumePercentage: {
      sql: `value`,
      type: `number`,
      description: `How full is the bin`,
    },
    measuredOn: {
      sql: `measured_on`,
      type: `time`,
    }
  },

  preAggregations: {

  }
})