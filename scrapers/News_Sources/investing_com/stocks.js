const { investing } = require('investing-com-api');
const fs = require('fs').promises; // Import the fs module

async function main() {
  try {

    const NASDAQ = await investing("20");
    const usTech100 = await investing("1175151");
    const SP500 = await investing("166");

    // Convert Millisecond timestamp to regular date format
    const convertTimestampToDate = (timestamp) => {
      const date = new Date(timestamp);
      // Format as ISO date string (e.g., "2024-04-11T00:00:00.000Z")
      return date.toISOString(); 
    };

    // Convert timestamps in the API response to regular date format
    NASDAQ.forEach(entry => {
      entry.date = convertTimestampToDate(entry.date);
    });

    usTech100.forEach(entry => {
      entry.date = convertTimestampToDate(entry.date);
    });

    SP500.forEach(entry => {
      entry.date = convertTimestampToDate(entry.date);
    })

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



