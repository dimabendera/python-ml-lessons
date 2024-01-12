const csv = require("fast-csv");
const tf = require("@tensorflow/tfjs");
require("@tensorflow/tfjs-node");

async function *dataGenerator(csvUrl="./data/train_dataset.csv",
                              targetColumn="target",
                              columns=[...Array(300).keys()].map(x => `f_${x}`),
                              limit=4096*4) {
    const stream = csv.parseFile(csvUrl, { headers: true });
    let i = 0;
    for await (let chunk of stream) {
        if (i > limit) {
            break;
        }
        i++;
        const ys = [Number(chunk[targetColumn])];
        const xs = columns.map(column => Number(chunk[column]));
        yield {xs, ys}
    }
}

async function main() {
    const model = tf.sequential({
        layers: [
            tf.layers.dense({inputShape: [300], units: 512, activation: 'relu'}),
            tf.layers.dense({units: 1, activation: 'relu'}),
        ]
    });
    model.summary()

    model.compile({
      optimizer: 'sgd',

      loss: tf.losses.meanSquaredError,
    });

    const countLines =  2_827_269;
    const batchSize = 4096;
    const countBatches = Math.ceil(countLines / batchSize);
    const ds = tf.data.generator(dataGenerator).batch(batchSize);

    // Train the model for 2 epochs.
    // onBatchEnd(batch, logs)
    await model.fitDataset(ds, {
        epochs: 2,
        callbacks: {onBatchEnd: (batch, logs) =>
                console.log(`batch ${batch} from ${countBatches} batches`)}});

    // Predict 3 random samples.
    const prediction = model.predict(tf.randomNormal([3, 300]));
    prediction.print();

    await model.save("file://model");
}

(async () => {
    await main();
})()
