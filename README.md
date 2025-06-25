# Web Tool Setup and Usage Guide

## Step 1: Install Required Libraries

Install the necessary libraries from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Step 2: Create Environment Configuration File

Create a `.env` file in the project root directory and add your Google API Key:

```bash
# Create .env file
touch .env
```

Open the `.env` file and add the following content:

```env
GOOGLE_API_KEY=Your_GOOGLE_API_Key
```

**Note:** Replace `Your_GOOGLE_API_Key` with your actual API key.

## Step 3: Launch Playwright MCP Server

Open a new terminal and run the following command:

```bash
npx @playwright/mcp@latest --port 3333
```

**Important:** Keep this terminal running throughout the entire usage process.

## Step 4: Use the Tool

After completing all the above steps, type the following command to start using:

```bash
adk web
```

## Troubleshooting

### Common Issues:

1. **Port 3333 already in use:**
   - Change to a different port: `npx @playwright/mcp@latest --port 3334`

2. **Google API Key not found:**
   - Check that the `.env` file has the correct format
   - Ensure there are no extra spaces

3. **Library installation errors:**
   - Update pip: `pip install --upgrade pip`
   - Use a virtual environment if needed

## Notes

- Ensure you have a stable internet connection
- The terminal running Playwright MCP must be kept open
- If you encounter errors, carefully recheck each step
