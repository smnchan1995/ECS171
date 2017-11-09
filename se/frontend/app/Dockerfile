FROM node:8

# Remove the outdated version of yarn that is installed by the node image
RUN rm -f /usr/local/bin/yarn

# Install yarn package manager
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-key adv --keyserver pgp.mit.edu --recv D101F7899D41F3C3 \
  && apt-get update -qq && apt-get install -y -qq yarn \
  && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/

# Install node-gyp
RUN npm install -g node-gyp

# Copy the current directory to the client directory.
COPY ./public /client
COPY ./src /client

# Set the working directory to the client directory.
WORKDIR /client

# Run yarn install: install the app.
RUN yarn install

# Run yarn build: generate the /build/ folder.
RUN yarn build

# Expose port 3000.
# EXPOSE 3000

# Run the app.
# CMD ["mkdir", "-p", "image_build_dir"]
# CMD ["mv", "build/*", "image_build_dir"]
