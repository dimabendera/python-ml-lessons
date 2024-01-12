const csv = require("fast-csv");
const tf = require("@tensorflow/tfjs");
let gaussian = require('gaussian');
require("@tensorflow/tfjs-node");

async function *dataGenerator(csvUrl="./data/test_dataset.csv",
                              targetColumn="target",
                              columns=[...Array(300).keys()].map(x => `f_${x}`)) {
    const stream = csv.parseFile(csvUrl, { headers: true });
    for await (let chunk of stream) {
        const ys = [Number(chunk[targetColumn])];
        const xs = columns.map(column => Number(chunk[column]));
        yield {xs, ys}
    }
}

async function main() {
    const model = await tf.loadLayersModel('file://model/model.json');
    model.summary()

    // Predict 3 random samples.
    const prediction = model.predict(tf.randomNormal([3, 300]));
    prediction.print();

    model.compile({
      optimizer: tf.train.adam(0.001),

      loss: tf.losses.meanSquaredError,
    });
    const batchSize = 4096;
    const ds = tf.data.generator(dataGenerator).batch(batchSize);
    const res = await model.evaluateDataset(ds, {
        batches: batchSize,
    });

    let mean = 1,
        variance = 0.15;
    let distribution = gaussian(mean, variance);
    let grade = (1 - distribution.cdf(res.dataSync()[0]))*10;
    console.log("Your grade", grade)

}

(async () => {
    await main();
})()

