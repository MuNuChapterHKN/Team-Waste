-- first island
INSERT INTO threekeco.island (name)
VALUES ('prima');

-- first bin type 1
-- types: 1 - glass & can, 2 - organic/compostable, 3 - paper, 4 - plastic, 5 - waste
INSERT INTO threekeco.bin (island_id, type)
VALUES (1, 1);

-- first sensor type 1
-- types: 1 - infrared, 2 - load, 3 - volume
INSERT INTO threekeco.sensor (bin_id, type)
VALUES (1, 1);