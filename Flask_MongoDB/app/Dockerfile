# Use an official Node runtime
FROM node:25-alpine

# Set the working directory in the container to /react-app
WORKDIR /react-app

# Copy package.json and package-lock.json
COPY package*.json ./
RUN npm install

# Create a non-root user to run the application
RUN adduser -D reactuser

# Change ownership of the /react-app/node_modules directory to the non-root user
RUN chown -R reactuser:reactuser /react-app/node_modules

# Switch to the non-root user
USER reactuser

# Make port 5173 available to the world outside this container
EXPOSE 5173

# Run npm run dev when the container launches
CMD ["npm", "run", "dev", "--", "--host=0.0.0.0"]
