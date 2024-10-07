# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- insertion marker -->
## Unreleased

<small>[Compare with latest](https://github.com/mjanez/ckan-docker/compare/v2.9.11-stable...HEAD)</small>

### Added

- Add patch to fix ckanext-pages ([a646b49](https://github.com/mjanez/ckan-docker/commit/a646b491251c3554230f488f4b2ac6b4bd9ae4f8) by mjanez).
- Add docs about ckanet-schemingdcat harvesters. ([7136656](https://github.com/mjanez/ckan-docker/commit/71366560b32b5e6e6de7a2e26ec1b93afde6cd46) by mjanez).

### Fixed

- Fix CKAN xloader API token creation ([05edcca](https://github.com/mjanez/ckan-docker/commit/05edcca600a64c8a0fb269c1d1dd034c8808fbec) by mjanez).
- Fix start_ckan.sh.override for clearer CSRF check and update PROXY_SERVER_URL in .env.codespaces ([d312797](https://github.com/mjanez/ckan-docker/commit/d31279779b432edf69cfc0e2a354895bb4c55ff2) by mjanez).

### Removed

- Remove --plugins options from uWSGI configuration ([3fdab45](https://github.com/mjanez/ckan-docker/commit/3fdab45448d5372bd5e1e2eb9bb4f34a5e2b3e83) by mjanez).
- Remove unnecessary files related to updating who.ini ([ae97c91](https://github.com/mjanez/ckan-docker/commit/ae97c9120b5bab908a1e8985d112639d23789618) by mjanez).
- Remove unnecesary who.ini config ([6adab9d](https://github.com/mjanez/ckan-docker/commit/6adab9d26294b8f115c4f4a9e471dde4aefdcad2) by mjanez).

<!-- insertion marker -->
## [v2.9.11-stable](https://github.com/mjanez/ckan-docker/releases/tag/v2.9.11-stable) - 2024-08-29

<small>[Compare with v2.9.9-stable](https://github.com/mjanez/ckan-docker/compare/v2.9.9-stable...v2.9.11-stable)</small>

### Added

- Add CKANEXT__SCHEMINGDCAT_ENDPOINTS_YAML ([dc3032d](https://github.com/mjanez/ckan-docker/commit/dc3032d37cef6c60ce9e4b056297539b578d2511) by mjanez).
- Add info to include dev mode and clone CKAN extensions with specific tags. ([c402d5a](https://github.com/mjanez/ckan-docker/commit/c402d5a38d92f1ed0fe234af04070a9f8be69077) by mjanez).
- Add info  to clone CKAN extensions with specific tags, update reqs and autoclrf for dev mode ([274861a](https://github.com/mjanez/ckan-docker/commit/274861a28a19db85954456e166b8e3c0ad53232e) by mjanez).
- Add new fields to solr schema file ([37ed4c1](https://github.com/mjanez/ckan-docker/commit/37ed4c163e267def27e322bbd56cd1d8b8df6daf) by mjanez).
- Add slug-preview patch ([3a51ddd](https://github.com/mjanez/ckan-docker/commit/3a51ddd8295c42e74340bf1d697f0ee76fd37dde) by mjanez).
- Add .env docs ([f19de7e](https://github.com/mjanez/ckan-docker/commit/f19de7eb1a41dd210291c0d48b62b10eab200d16) by mjanez).
- Add CORS envvars ([fa50127](https://github.com/mjanez/ckan-docker/commit/fa501274f0a42e68010a096a7370dae9ff85d243) by mjanez).
- Add Docker workflow for building and pushing ckan-docker image from master push ([28602e0](https://github.com/mjanez/ckan-docker/commit/28602e0f0c08bca8d18e8f689bc0e96c5f30a74a) by mjanez).
- Add crond in background ([c1b819b](https://github.com/mjanez/ckan-docker/commit/c1b819b624cdf909962d9ccf444ec33c2681143c) by mjanez).
- Add harvest & xloader worker configuration ([68a9ce9](https://github.com/mjanez/ckan-docker/commit/68a9ce9eccde43ec130e0148cf3282441bd91a03) by mjanez).
- Add init script for configuring datapusher ([e439eda](https://github.com/mjanez/ckan-docker/commit/e439eda620939709e38037a3dba295e991f1db5c) by amercader).
- Add step to copy init files ([f9ebc0c](https://github.com/mjanez/ckan-docker/commit/f9ebc0c41c1bda1bfac992d5687e15c81e2c5e80) by amercader).

### Fixed

- Fix for ckanext-dcat v1.80 and ckanext-schemingdcat v3.2.2 ([35a6bdc](https://github.com/mjanez/ckan-docker/commit/35a6bdc56efe0c560b065d4a904643f1b3a6314d) by mjanez).
- Fix dataset_scope field type ([11d7b9e](https://github.com/mjanez/ckan-docker/commit/11d7b9ef1772dd24f790c94add05ac87a92248f3) by mjanez).
- Fix 02_setup_scheming.sh ([4cecf1a](https://github.com/mjanez/ckan-docker/commit/4cecf1a9d1d94a2087d430a8e892f6a90406425e) by mjanez).
- Fix notes/tips ([176a18a](https://github.com/mjanez/ckan-docker/commit/176a18a2ef25b38fb9d78fa79e8cf1db174e8067) by mjanez).
- Fix dev mode ([c678a29](https://github.com/mjanez/ckan-docker/commit/c678a294ecf1d11bcb23715d723b88a12970a0ac) by mjanez).
- Fix dev networks bug ([1d87acc](https://github.com/mjanez/ckan-docker/commit/1d87acc1243b4ae0285cdb1fe6ea8601170a0d59) by mjanez).
- Fix depends_on ckan-dev ([501f2d2](https://github.com/mjanez/ckan-docker/commit/501f2d209bac2d7b21621bff42298b68043fe95e) by mjanez).
- fix readme toc, headings, replace one screenshot of text ([32af5cf](https://github.com/mjanez/ckan-docker/commit/32af5cfbf8d1c81fd7e309d158117445067a8f13) by Ian Ward).
- Fix restore backups and plugin creation docs ([1a44ca5](https://github.com/mjanez/ckan-docker/commit/1a44ca5b8484821c39ec83c624cc5a486c2f1e66) by mjanez).
- Fix Dockerfile to install requirements for ckanext-schemingdcat ([efefb73](https://github.com/mjanez/ckan-docker/commit/efefb7338ec0bbc83421303f5a5be5a1b85c1bca) by mjanez).
- Fix scheming_dcat to schemingdcat ([f08177a](https://github.com/mjanez/ckan-docker/commit/f08177a55e60acee2b6edcf69297048556f80916) by mjanez).
- Fix supervisord command in start_ckan_development.sh.override ([c2c1ef6](https://github.com/mjanez/ckan-docker/commit/c2c1ef60040d56c665f3862afb7524d3304c68c5) by mjanez).
- Fix token revocation in 01_setup_xloader.sh ([96a4c39](https://github.com/mjanez/ckan-docker/commit/96a4c394a74bd7c62031f52f4c9902055c03414e) by mjanez).
- Fix image tag in the Dev Dockerfile ([5fc1efc](https://github.com/mjanez/ckan-docker/commit/5fc1efce33dd6d752660dac3752d0c144c5a90cc) by amercader).
- fixed line endings for windows ([bb936fa](https://github.com/mjanez/ckan-docker/commit/bb936fab7ab2c2661d1e7dc455098dd58c5afdd8) by Hendrik Lücke-Tieke).

### Removed

- remove broken, confusing CKAN_PORT setting ([18fbe44](https://github.com/mjanez/ckan-docker/commit/18fbe445c1782d887f6ac77813e507d529246b53) by Ian Ward).
- Remove unused harvest patch ([f033f6b](https://github.com/mjanez/ckan-docker/commit/f033f6b10c2f5b88205928b6a9df93327f9f4611) by mjanez).
- remove container names ([445d525](https://github.com/mjanez/ckan-docker/commit/445d52555de0567d7b9f40e53ba2621ec2494598) by Ian Ward).
- Remove unnecesary TODO ([7309d15](https://github.com/mjanez/ckan-docker/commit/7309d15bc0e8d91a245cef01a938fb762a2ef7d2) by mjanez).
- Remove timezone commands ([f653b03](https://github.com/mjanez/ckan-docker/commit/f653b0324de14e83d5fc0e26dc72c2ec714de4be) by amercader).
- remove container_name? ([2a8f844](https://github.com/mjanez/ckan-docker/commit/2a8f844ecf5564b63a3430924e8bacdc91e40c30) by Ian Ward).

## [v2.9.9-stable](https://github.com/mjanez/ckan-docker/releases/tag/v2.9.9-stable) - 2024-02-12

<small>[Compare with v2.9.8-stable](https://github.com/mjanez/ckan-docker/compare/v2.9.8-stable...v2.9.9-stable)</small>

### Added

- Add info about ckanext-scheming_dcat ([da0f7b6](https://github.com/mjanez/ckan-docker/commit/da0f7b66d5198859e9af5ca2cfd0a7a279d20261) by mjanez).
- Add ckanext-fluent ([7eb35dc](https://github.com/mjanez/ckan-docker/commit/7eb35dc37084867fb8e115a932bc8c0fad6ca9c8) by mjanez).
- Add hadolint no-fail ([99b4376](https://github.com/mjanez/ckan-docker/commit/99b437691cf8046a742a6ab667fe6d48395a7a70) by mjanez).
- Add ckanext-pages patch for root_path ([5d9ad91](https://github.com/mjanez/ckan-docker/commit/5d9ad919c2f22724d074ae330d1a8e8618751d89) by mjanez).
- Add multiple Dockerfiles to hadolint ([2c99632](https://github.com/mjanez/ckan-docker/commit/2c99632c1d285b00a7b3fc0e32d7f8a911cf096a) by mjanez).
- Add hadolint to Dockerfile.ghcr image ([3c9d916](https://github.com/mjanez/ckan-docker/commit/3c9d9166f1542ce2f1f592ef7ab2893f51d19189) by mjanez).
- Add :test-build-only tag ([c8eb770](https://github.com/mjanez/ckan-docker/commit/c8eb770920f4dd527ac278498abcf86b1b5dd8e0) by mjanez).
- Add docker-manual action and logo to README ([66e231b](https://github.com/mjanez/ckan-docker/commit/66e231b343a72ecf0074323f307ebded20d9d3b7) by mjanez).
- Add CKANEXT__DCAT__DEFAULT_CATALOG_ENDPOINT ennvar ([e5447ef](https://github.com/mjanez/ckan-docker/commit/e5447ef32b2bd6a9ce420c74ba357f6ca213b6b4) by mjanez).
- Add geometadata_base_uri ennvar ([8392b0a](https://github.com/mjanez/ckan-docker/commit/8392b0a72fb64f900dbf52fbd8e4ef2b6f4bc9a8) by mjanez).
- Added Copying and License in README.md ([c0e6217](https://github.com/mjanez/ckan-docker/commit/c0e62170578616c73423bbb4c5c7eed80535da95) by GauravPandey-NECI).
- Add entrypoint for ckanext-pages ([09f56eb](https://github.com/mjanez/ckan-docker/commit/09f56ebce605c39030048b665caa802b1fe66bed) by mjanez).
- Add CKAN backup scripts ([5fbd5e6](https://github.com/mjanez/ckan-docker/commit/5fbd5e64b3632a6364f31bea58d2f4f90afb299c) by mjanez).
- Added steps for user creation ([6e92dee](https://github.com/mjanez/ckan-docker/commit/6e92deebfa94a957f82779a77f7f020cedbcfd3e) by GauravPandey-NECI).

### Fixed

- Fix bash script to backup ckan db ([49b9be0](https://github.com/mjanez/ckan-docker/commit/49b9be0c3b4057b17ae5e7370a61c2f4e2fe6d00) by mjanez).
- Fix tag name ([4c0c627](https://github.com/mjanez/ckan-docker/commit/4c0c627f8b7e84ee43a0cadbcdc607c467583f40) by mjanez).
- Fix Dockerfiles ([8a599a1](https://github.com/mjanez/ckan-docker/commit/8a599a11a4285eb15bb4f0e67bb680259f1cf080) by mjanez).
- Fix docker build context ([89610da](https://github.com/mjanez/ckan-docker/commit/89610daec4084e775bed1fd17eb20dd56054ddbd) by mjanez).
- Fix dockerfile images ([712abb1](https://github.com/mjanez/ckan-docker/commit/712abb16b2ffb955988f087a3995a7409b8462fa) by mjanez).
- Fix actions ([42d2ddb](https://github.com/mjanez/ckan-docker/commit/42d2ddb91c7144540f95401b3f3353d53e834d80) by mjanez).
- Fix docker-pr ([21b0902](https://github.com/mjanez/ckan-docker/commit/21b09029593c699b4230482a9e57ef6fb755bf21) by mjanez).
- Fix image ([a6d9194](https://github.com/mjanez/ckan-docker/commit/a6d9194f3014a45cd18d21b0232f05d0ed8a869e) by mjanez).
- Fix host_ports/ports in Apache/NGINX Dockerfiles ([39611be](https://github.com/mjanez/ckan-docker/commit/39611bec41b02052a4ba7633d3ad1c9a403bda16) by mjanez).
- Fix ckan-pycsw service ([94573c4](https://github.com/mjanez/ckan-docker/commit/94573c4290b57877735bdfc470b83d6834fa8e2b) by mjanez).
- Fix non-root user execution of ckan-pycsw ([f86e1be](https://github.com/mjanez/ckan-docker/commit/f86e1be5a5ed4433272c51a4fc1c29be91a4e67d) by mjanez).
- Fix map attribution ([eea2a8b](https://github.com/mjanez/ckan-docker/commit/eea2a8b4aad91595aed130ee93fac0dc7661fe00) by mjanez).
- Fix ckan-pycsw entrypoint ([f578862](https://github.com/mjanez/ckan-docker/commit/f578862769023f8d1a59a826313e46c95b77cfb0) by mjanez).
- Fix script extension ([43ca2b6](https://github.com/mjanez/ckan-docker/commit/43ca2b6a4e7f4364489b95d42f4e8ccb837cc530) by avdata99).
- Fix default .env.example ([77719fd](https://github.com/mjanez/ckan-docker/commit/77719fd2ebf56a9743cc1cd1e5e9d4439393e915) by mjanez).
- Fix 05_setup_pages.sh ([145b53f](https://github.com/mjanez/ckan-docker/commit/145b53ffaf3ddaa9722a883f14c56fd9698fefba) by mjanez).
- Fix docker-compose and remove Solr image ([5e3baba](https://github.com/mjanez/ckan-docker/commit/5e3baba522bbc0cbcaf59e943aed88df2fc1f429) by mjanez).
- Fix nginx exposed ports ([1be9948](https://github.com/mjanez/ckan-docker/commit/1be99482fa943440967dc2ec0d856bebfd2afbd4) by mjanez).
- Fix multilocations ([7ea93fc](https://github.com/mjanez/ckan-docker/commit/7ea93fcb9b4143813ab102948a5ad71af661b628) by mjanez).
- Fix postgresql entrypoint ([2c1f12e](https://github.com/mjanez/ckan-docker/commit/2c1f12e790cf7e548a6dcb7aad4c3c19ee69ca2f) by mjanez).
- Fix env files ([cf18c31](https://github.com/mjanez/ckan-docker/commit/cf18c31492b844594606ee8137ee41a1f1708572) by mjanez).
- Fix Dockerfile plugins ([922edc7](https://github.com/mjanez/ckan-docker/commit/922edc720cf611a7027bad76da2219fb47569e50) by mjanez).
- Fix dev image ([754711c](https://github.com/mjanez/ckan-docker/commit/754711c83779c29d2fa1ef8a7c777b4c2f66863f) by mjanez).
- Fix nginx image ([b2b2761](https://github.com/mjanez/ckan-docker/commit/b2b27613286d5897ee3e1847eabf8e04d0f420e4) by mjanez).
- Fix who.ini when is only: "/" ([a2fa917](https://github.com/mjanez/ckan-docker/commit/a2fa91798b7b812a1ead9928b70d7c43da5dc7c3) by mjanez).
- Fix nginx multiple locations ([eba3896](https://github.com/mjanez/ckan-docker/commit/eba3896b44cd2b632a9879ebf8e33bd6966c54a6) by mjanez).
- Fix README ([93831d9](https://github.com/mjanez/ckan-docker/commit/93831d96f240c9fabbdcfa8ca6d6e60804702f3f) by mjanez).

### Removed

- Remove hadolint when build & push ([5de535d](https://github.com/mjanez/ckan-docker/commit/5de535d018748532528f0aea33af71c0cf2fe490) by mjanez).
- Remove unnecesary patch ([4b1e735](https://github.com/mjanez/ckan-docker/commit/4b1e735fea2a95ff914239be87e4c139abfed5d0) by mjanez).
- Remove ckanext-sparql_interface ([30b699f](https://github.com/mjanez/ckan-docker/commit/30b699f4d7811dc98f284a9898799c112799bfd7) by mjanez).
- remove .env file ([aed9916](https://github.com/mjanez/ckan-docker/commit/aed99166ce4dbc7c6becb20b1f36941c87ae7fd4) by Brett).

## [v2.9.8-stable](https://github.com/mjanez/ckan-docker/releases/tag/v2.9.8-stable) - 2023-05-09

<small>[Compare with first commit](https://github.com/mjanez/ckan-docker/compare/17c07d99ff636b0899f5f4fc05795f6bbf6ba672...v2.9.8-stable)</small>

### Added

- Add ckanext-facet_scheming ([eeeb652](https://github.com/mjanez/ckan-docker/commit/eeeb652acee1a8e6353d5199127415da0dcf0969) by mjanez).
- Add README.md to log/ and metadata/ ([5c3a97e](https://github.com/mjanez/ckan-docker/commit/5c3a97ea8c1dd55db8adae5e4f24b8ab9c348d8c) by mjanez).
- Add Dockerfile.ghcr ([de06443](https://github.com/mjanez/ckan-docker/commit/de0644318e2cd6cab46bdfbf096f210baa4fafa4) by mjanez).
- Add resourcedictionary ckan patch ([c0db947](https://github.com/mjanez/ckan-docker/commit/c0db94798742f9590e184f4f823ff6a3fff64f8b) by mjanez).
- Add logging to docker compose files ([25b49de](https://github.com/mjanez/ckan-docker/commit/25b49de65c1b953c506b5ddd319754fca54f4a1c) by mjanez).
- Add info about images ([9053bec](https://github.com/mjanez/ckan-docker/commit/9053becc76466e4d77d2e833dbb7c255388ae819) by mjanez).
- Add ckan-pycsw & httpd (RDF/CSW) bundle ([7a39ea5](https://github.com/mjanez/ckan-docker/commit/7a39ea5f410a6ef2a607e13a00e8cafe8f3b7f02) by mjanez).
- Add solr8-spatial image ([5357b1f](https://github.com/mjanez/ckan-docker/commit/5357b1f64f1f13e60170c6d2a5a8d9cba9a18739) by mnjnz).
- Add custom images of base Dockerfiles ([53d2d65](https://github.com/mjanez/ckan-docker/commit/53d2d65cb10d22af216a6e132aa552090dc08d21) by mnjnz).
- Add entrypoints - ckanext-dcat - previews - ckanext-xloader ([4985c8b](https://github.com/mjanez/ckan-docker/commit/4985c8befc9f1c33bb04b8a6f8dd80ea4555aed8) by mjanez).
- Add warning info about this repo ([64195b5](https://github.com/mjanez/ckan-docker/commit/64195b52e8d7e6c9056900b874bc1fd526d78b3a) by mjanez).
- Added enable-threads to Datapusher ([3522bf5](https://github.com/mjanez/ckan-docker/commit/3522bf54c301730a8fd2496d499b89b0517fb50c) by Brett).
- Added Sphinx doc (initial commit) ([5643f06](https://github.com/mjanez/ckan-docker/commit/5643f067de844580e4df5160f2a30124c22815d0) by Clément MOUCHET).
- Added missing Dockerfile ([3cd3b50](https://github.com/mjanez/ckan-docker/commit/3cd3b50fad50f71c29a46e344fea2028b5e27cef) by Clément MOUCHET).
- ADDED: - Data only container for Postgres db & CKAN FileStore - Nginx container (still based on official container, but copies the config for portability) UPDATED: - Postgres Dockerfile to allow custom PGDATA directory & initiate it if it's not there or is empty - fig.ml to reflect the latest changes (datapusher, nginx, data container) ([3946774](https://github.com/mjanez/ckan-docker/commit/39467745f1395d52143890a1e11488fedab0d457) by Clément MOUCHET).

### Fixed

- Fix README ([b362ad8](https://github.com/mjanez/ckan-docker/commit/b362ad8e2fc8c93205484b2a0db226b03beee800) by mjanez).
- Fix Dockerfile.dev and add info to doc ([65c038a](https://github.com/mjanez/ckan-docker/commit/65c038afd0c118cca94672225c9c5fa1249f5948) by mjanez).
- Fix development mode ([0ba0561](https://github.com/mjanez/ckan-docker/commit/0ba0561f3189c8a946cb2431dfffac4fcd8c730c) by mjanez).
- Fix cronjobs by use scheduler ([f16a527](https://github.com/mjanez/ckan-docker/commit/f16a5270027e5960e2ddc3a1b8f88101426769da) by mjanez).
- Fix image names ([3d7c418](https://github.com/mjanez/ckan-docker/commit/3d7c4182bee1e3ac478481988d9efd58d6238b19) by mjanez).
- Fix xloader token creation ([3f90532](https://github.com/mjanez/ckan-docker/commit/3f90532d05fb3c0192060be6a49b23d833f29e03) by mjanez).
- Fix image ([05b1abe](https://github.com/mjanez/ckan-docker/commit/05b1abe4bd51c80d034aa9ca5c4e985014a3ab17) by mjanez).
- Fix APACHE_PROXY_PASS to APACHE_CKAN_PROXY_PASS ([9d47fec](https://github.com/mjanez/ckan-docker/commit/9d47feca615bfb5aef8be2a18885720ea9754a09) by mjanez).
- Fix CKAN_SITE_URLS in .env ([3152fd5](https://github.com/mjanez/ckan-docker/commit/3152fd5b48e2519d408acfec5f0ce6bfe33d6d65) by mjanez).
- Fix docker image tag ([af1ce41](https://github.com/mjanez/ckan-docker/commit/af1ce41a86936a87f385f01e3ffad6f51dfe3048) by mjanez).
- Fix workflows & docker compose files ([86b6486](https://github.com/mjanez/ckan-docker/commit/86b6486b7904418877d5508649ecbae2c8bbc9e4) by mnjnz).
- Fix docker.yml ([b222c09](https://github.com/mjanez/ckan-docker/commit/b222c0924aeed62d84c4b5e35de318d07e9dfc04) by mjanez).
- Fix .env.example ([4702b86](https://github.com/mjanez/ckan-docker/commit/4702b86449d8b27de0b1006e96ce229fea8c809e) by mnjnz).
- Fix xloader setup ([3ffba6f](https://github.com/mjanez/ckan-docker/commit/3ffba6fe0dc1c941f84dfa0a48d9467a5f9e3e6c) by mnjnz).
- Fix views ([d30bbad](https://github.com/mjanez/ckan-docker/commit/d30bbad8e96bc7f0d326dcc454eafa71d992be56) by mjanez).
- Fix setup worker ([4240356](https://github.com/mjanez/ckan-docker/commit/424035617f2f3a541f21e89b964eac2a11804a9e) by mjanez).
- Fix setup_xloader ([f50edb4](https://github.com/mjanez/ckan-docker/commit/f50edb467a305d94a8920262a55874b49752a98d) by mjanez).
- Fix Dockerfile ([cd3dfa0](https://github.com/mjanez/ckan-docker/commit/cd3dfa0985875ede8f28fd5713b2a08cefc3df5a) by mjanez).
- Fix link to CKAN Docs ([309078d](https://github.com/mjanez/ckan-docker/commit/309078d3e546002de66bce3474063c64bd1af3b5) by mjanez).
- fixed path of datapusher ([dbc7561](https://github.com/mjanez/ckan-docker/commit/dbc7561a5e7324018122845822e01680dd9d2547) by tajima).

### Changed

- changed default port to avoid CORS issues ([1750619](https://github.com/mjanez/ckan-docker/commit/1750619291e73db6258395a5026ee0b55c1b37de) by Clément MOUCHET).

### Removed

- Remove solr build ([e0eb54f](https://github.com/mjanez/ckan-docker/commit/e0eb54f61f7fe0a62fdb471439d16a339e4aa915) by mnjnz).
- Remove datapusher - Datapusher out of date with ckanext-xloader - Fix deprecated views ([7db1611](https://github.com/mjanez/ckan-docker/commit/7db161188eaa8d210b7b818c5cbdde92a8fcd53c) by mjanez).
- Remove datapusher ([c61176e](https://github.com/mjanez/ckan-docker/commit/c61176e20cc612a6ba00b6e998e8f371e17d9c65) by mjanez).
- Remove images directory + TODO's file ([7e24429](https://github.com/mjanez/ckan-docker/commit/7e244290a5d436ecf1ac00a51051825d550f1608) by Brett).
- Remove pdf_view from default plugins ([dcf7b52](https://github.com/mjanez/ckan-docker/commit/dcf7b52039d9e2ccb443ed9056842f4c99e131c3) by Matt).

