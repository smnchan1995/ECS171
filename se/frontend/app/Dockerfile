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

# Copy the needed files to the base_dir directory. COPY does not behave like CLI cp: you need to specify a directory to create.
COPY ./public/ /base_dir/public/
COPY ./src/ /base_dir/src/
COPY ./package.json /base_dir/

# Set the working directory to the base_dir directory.
WORKDIR /base_dir/

# Make the temporary image build directory.
RUN mkdir -p image_build_dir

# Remove the contents of the directory, if they exist.
RUN rm -rf image_build_dir/*

# Run yarn install: install the app.
RUN yarn install

# Run yarn build: generate the /build/ folder.
RUN yarn build
