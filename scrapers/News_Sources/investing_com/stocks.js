const { investing } = require('investing-com-api');
const fs = require('fs').promises; // Import the fs module

async function main() {
  try {

    const NASDAQ = await investing("20");
    const usTech100 = await investing("1175151");
    const SP500 = await investing("166");

    // Convert responses to JSON with indentation
    const jsonContent = JSON.stringify({ NASDAQ, usTech100, SP500 }, null, 4);

    // Write formatted JSON to a file
    await fs.writeFile('stockresults.txt', jsonContent);

    console.log('Responses written to stockresults.txt file.');

  } catch (err) {
    console.error(err);
  }


}


main();



