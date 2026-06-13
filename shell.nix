{pkgs ? import (import ./lon.nix).nixpkgs {}}:
pkgs.mkShellNoCC {
  packages = [
    pkgs.nil
    pkgs.alejandra
    pkgs.ty
    pkgs.ruff
    (pkgs.python3.withPackages (p:
      with p; [
        requests
      ]))
  ];
}
