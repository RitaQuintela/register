// serverless function (e.g., AWS Lambda)
const XLSX = require('xlsx');

exports.handler = async (event) => {
    try {
        const workbook = XLSX.readFile('tuition_fees.xlsx');
        const sheetName = workbook.SheetNames[0];
        const worksheet = workbook.Sheets[sheetName];

        // Assuming program names are in column A and fees in column B
        const data = XLSX.utils.sheet_to_json(worksheet);
        const programName = event.queryStringParameters.programName.toLowerCase();
        const program = data.find(item => item.program.toLowerCase() === programName);

        if (program) {
            const tuition = program.fee;
            return {
                statusCode: 200,
                body: JSON.stringify({ tuition })
            };
        } else {
            return {
                statusCode: 400,
                body: JSON.stringify({ error: 'Invalid program choice' })
            };
        }
    } catch (error) {
        return {
            statusCode: 500,
            body: JSON.stringify({ error: 'Internal server error' })
        };
    }
};
