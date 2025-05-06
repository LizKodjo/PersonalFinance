# Use Node base image
FROM node:20

# Set working directory
WORKDIR /app

# Install dependencies early to leverage Docker cache
COPY package*.json ./
RUN npm install

# Copy source code
COPY . .

# Expose the Next.js dev server port
EXPOSE 3010

# Start the Next.js development server
CMD ["npm", "run", "dev"]
