# Azure App Service Deployment Guide

## Prerequisites
1. Azure subscription
2. Azure CLI installed: `az login`

## Option 1: Azure SQL Database (Recommended for Azure)

### Step 1: Create Azure SQL Database
```bash
# Create resource group
az group create --name blogfast-rg --location eastus

# Create SQL Server
az sql server create \
  --name blogfast-sql-server \
  --resource-group blogfast-rg \
  --location eastus \
  --admin-user sqladmin \
  --admin-password YourStrongPassword123!

# Create database
az sql db create \
  --resource-group blogfast-rg \
  --server blogfast-sql-server \
  --name blogfast-db \
  --service-objective S0

# Allow Azure services
az sql server firewall-rule create \
  --resource-group blogfast-rg \
  --server blogfast-sql-server \
  --name AllowAzureServices \
  --start-ip-address 0.0.0.0 \
  --end-ip-address 0.0.0.0
```

### Step 2: Create App Service
```bash
# Create App Service plan
az appservice plan create \
  --name blogfast-plan \
  --resource-group blogfast-rg \
  --sku B1 \
  --is-linux

# Create web app
az webapp create \
  --resource-group blogfast-rg \
  --plan blogfast-plan \
  --name blogfast-app \
  --runtime "PYTHON:3.11"
```

### Step 3: Configure Environment Variables
```bash
# Generate a new secret key
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Set app settings
az webapp config appsettings set \
  --resource-group blogfast-rg \
  --name blogfast-app \
  --settings \
    SECRET_KEY="your-generated-secret-key" \
    DEBUG="False" \
    ALLOWED_HOSTS="blogfast-app.azurewebsites.net" \
    DB_ENGINE="azure-sql" \
    DATABASE_NAME="blogfast-db" \
    DATABASE_USER="sqladmin" \
    DATABASE_PASSWORD="YourStrongPassword123!" \
    DATABASE_HOST="blogfast-sql-server.database.windows.net" \
    DATABASE_PORT="1433" \
    SCM_DO_BUILD_DURING_DEPLOYMENT="true"
```

### Step 4: Deploy Application
```bash
# Initialize git (if not already)
cd /home/isaac/Desktop/blogfast
git init
git add .
git commit -m "Initial commit"

# Get deployment credentials
az webapp deployment source config-local-git \
  --name blogfast-app \
  --resource-group blogfast-rg

# Add Azure remote and push
git remote add azure <git-url-from-previous-command>
git push azure main
```

### Step 5: Run Migrations
```bash
# SSH into the app
az webapp ssh --name blogfast-app --resource-group blogfast-rg

# Inside SSH session:
source antenv/bin/activate
python manage.py migrate
python manage.py createsuperuser
exit
```

## Option 2: Azure Database for PostgreSQL

Follow similar steps but use:
```bash
# Create PostgreSQL server
az postgres flexible-server create \
  --name blogfast-postgres \
  --resource-group blogfast-rg \
  --location eastus \
  --admin-user pgadmin \
  --admin-password YourStrongPassword123! \
  --sku-name Standard_B1ms \
  --tier Burstable \
  --storage-size 32

# Create database
az postgres flexible-server db create \
  --resource-group blogfast-rg \
  --server-name blogfast-postgres \
  --database-name blogfast
```

Set environment:
```bash
DB_ENGINE="postgresql"
DATABASE_NAME="blogfast"
DATABASE_USER="pgadmin"
DATABASE_PASSWORD="YourStrongPassword123!"
DATABASE_HOST="blogfast-postgres.postgres.database.azure.com"
DATABASE_PORT="5432"
```

## Important Files for Deployment

Your app now includes:
- `requirements.txt` - All dependencies
- `.env.example` - Configuration template
- WhiteNoise - Static file serving
- Gunicorn - Production server

## Post-Deployment
1. Visit: `https://blogfast-app.azurewebsites.net`
2. Login: `https://blogfast-app.azurewebsites.net/accounts/login/`
3. Dashboard: `https://blogfast-app.azurewebsites.net/dashboard/`

## Cost Estimate (Monthly)
- App Service B1: ~$13
- Azure SQL S0: ~$15
- Total: ~$28/month

Or use PostgreSQL Flexible Server (Burstable): ~$10-15/month
