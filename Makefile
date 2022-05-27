#certora-vat	:;certoraRun --solc ~/.solc-select/artifacts/solc-0.8.13 Vat.sol --verify Vat:certora/Vat.spec --rule_sanity $(if $(rule),--rule $(rule),) --multi_assert_check
certora-vat	:;certoraRun --solc ~/.solc-select/artifacts/solc-0.8.13 Vat.sol --verify Vat:Vat.spec --rule_sanity --multi_assert_check
