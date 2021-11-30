FROM node:12.18.4

WORKDIR '/app'

COPY package.json .

# Run the command inside your image filesystem.
RUN npm install

EXPOSE 3000
# Copy the rest of your app's source code from your host to your image filesystem.
COPY . .

# Run the specified command within the container.
CMD [ "npm", "start" ]