# fund-eq-of-dai-certora
Succinctly prove the fundamental equation of DAI failed to hold using the Certora prover. The bug was fixed.

## Instructions
1. Install [Certora CLI](https://certora.atlassian.net/wiki/spaces/CPD/pages/7274497/Installation+of+Certora+Prover)
2. Install [solc-select](https://pypi.org/project/solc-select/)
3. Use solc-select to install solc 0.8.13 via `solc-select install 0.8.13`
4. Clone this repository via `git clone https://github.com/kmbarry1/fund-eq-of-dai-certora.git`
5. Run via `make certora-vat`
