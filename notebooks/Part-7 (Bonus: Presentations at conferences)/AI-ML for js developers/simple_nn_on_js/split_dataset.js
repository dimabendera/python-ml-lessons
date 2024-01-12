const fs = require('fs');
const csvSplitStream = require('csv-split-stream');

async function main() {

    const indexes = ["train_dataset", "test_dataset"]

    csvSplitStream.split(
      fs.createReadStream('data/train.csv'),
      {
        lineLimit: 2827269
      },
      (index) => fs.createWriteStream(`data/${indexes[index]}.csv`)
    )
    .then(csvSplitResponse => {
      console.log('csvSplitStream succeeded.', csvSplitResponse);
    }).catch(csvSplitError => {
      console.log('csvSplitStream failed!', csvSplitError);
    });

}

(async () => {
    await main();
})()
