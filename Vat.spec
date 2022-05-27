// Vat.spec

methods {
    Art(bytes32) returns (uint256) envfree
    art(bytes32, address) returns (uint256) envfree
    can(address, address) returns (uint256) envfree
    dai(address) returns (uint256) envfree
    debt() returns (uint256) envfree
    dust(bytes32) returns (uint256) envfree
    gem(bytes32, address) returns (uint256) envfree
    ilks(bytes32) returns (uint256, uint256, uint256, uint256, uint256) envfree
    ink(bytes32, address) returns (uint256) envfree
    Line() returns (uint256) envfree
    line(bytes32) returns (uint256) envfree
    live() returns (uint256) envfree
    rate(bytes32) returns (uint256) envfree
    sin(address) returns (uint256) envfree
    spot(bytes32) returns (uint256) envfree
    urns(bytes32, address) returns (uint256, uint256) envfree
    vice() returns (uint256) envfree
    wards(address) returns (uint256) envfree
}

ghost sumOfVaultDebtGhost() returns uint256 {
    init_state axiom sumOfVaultDebtGhost() == 0;
}

ghost mapping(bytes32 => uint256) rateGhost {
    init_state axiom forall bytes32 ilk. rateGhost[ilk] == 0;
}

ghost mapping(bytes32 => uint256) ArtGhost {
    init_state axiom forall bytes32 ilk. ArtGhost[ilk] == 0;
}

hook Sload uint256 v currentContract.ilks[KEY bytes32 ilk].(offset 0) STORAGE {
    require ArtGhost[ilk] == v;
}

hook Sstore currentContract.ilks[KEY bytes32 ilk].(offset 0) uint256 n (uint256 o) STORAGE {
    havoc sumOfVaultDebtGhost assuming sumOfVaultDebtGhost@new() == sumOfVaultDebtGhost@old() + (n * rateGhost[ilk]) - (o * rateGhost[ilk]);
    ArtGhost[ilk] = n;
}

hook Sload uint256 v currentContract.ilks[KEY bytes32 ilk].(offset 32) STORAGE {
    require rateGhost[ilk] == v;
}

hook Sstore currentContract.ilks[KEY bytes32 ilk].(offset 32) uint256 n (uint256 o) STORAGE {
    havoc sumOfVaultDebtGhost assuming sumOfVaultDebtGhost@new() == sumOfVaultDebtGhost@old() + (ArtGhost[ilk] * n) - (ArtGhost[ilk] * o);
    rateGhost[ilk] = n;
}

invariant fundamental_equation_of_dai()
   debt() == vice() + sumOfVaultDebtGhost()
   filtered { f -> !f.isFallback }
