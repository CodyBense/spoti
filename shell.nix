{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {

    packages = [
        (pkgs.python3.withPackages(pypkgs: with pypkgs; [
            requests
            python-dotenv
            pandas
            pandas-stubs
        ]))
    ];

    shellHook = ''
        echo Entered Python dev environment
    '';
}
