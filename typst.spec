Name:          typst
Version:       0.14.1
Release:       1
Summary:       A new markup-based typesetting system that is powerful and easy to learn.
License:       Apache-2.0
URL:           https://github.com/typst/typst
Source0:       %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: rust-packaging
BuildRequires: openssl 
BuildRequires: openssl-devel
BuildRequires: openssl-libs
BuildRequires: perl
BuildRequires: cargo-rpm-macros >= 24


%global debug_package %{nil}


%description
A new markup-based typesetting system that is powerful and easy to learn.


%prep
%autosetup


%build
export GEN_ARTIFACTS="artifacts" 
export RUSTFLAGS='-Copt-level=3'
cargo build -j${RPM_BUILD_NCPUS} -p typst-cli --release --locked


%install
# Binary
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 target/release/typst %{buildroot}%{_bindir}/%{name}
# Shell completion
install -Dpm 0644 crates/typst-cli/artifacts/%{name}.bash -t %{buildroot}%{bash_completions_dir}
install -Dpm 0644 crates/typst-cli/artifacts/%{name}.fish -t %{buildroot}%{fish_completions_dir}
install -Dpm 0644 crates/typst-cli/artifacts/_%{name}     -t %{buildroot}%{zsh_completions_dir}
# Manual pages
install -Dpm 0644 crates/typst-cli/artifacts/%{name}.1 -t %{buildroot}%{_mandir}/man1/
install -Dpm 0644 crates/typst-cli/artifacts/%{name}-compile.1 -t %{buildroot}%{_mandir}/man1/
install -Dpm 0644 crates/typst-cli/artifacts/%{name}-fonts.1 -t %{buildroot}%{_mandir}/man1/
install -Dpm 0644 crates/typst-cli/artifacts/%{name}-init.1 -t %{buildroot}%{_mandir}/man1/
install -Dpm 0644 crates/typst-cli/artifacts/%{name}-query.1 -t %{buildroot}%{_mandir}/man1/
install -Dpm 0644 crates/typst-cli/artifacts/%{name}-update.1 -t %{buildroot}%{_mandir}/man1/
install -Dpm 0644 crates/typst-cli/artifacts/%{name}-watch.1 -t %{buildroot}%{_mandir}/man1/

%files
%license LICENSE
%doc README.md
# Binaries
%{_bindir}/%{name}
# Shell completion
%{bash_completions_dir}/%{name}.bash
%{fish_completions_dir}/%{name}.fish
%{zsh_completions_dir}/_%{name}
# Manual pages
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-compile.1*
%{_mandir}/man1/%{name}-fonts.1*
%{_mandir}/man1/%{name}-init.1*
%{_mandir}/man1/%{name}-query.1*
%{_mandir}/man1/%{name}-update.1*
%{_mandir}/man1/%{name}-watch.1*

%changelog
* Sun Oct 26 2025 Ernesto Martínez <me@ecomaikgolf.com>

- typst 0.14.0

* Fri Sep 09 2025 Ernesto Martínez <me@ecomaikgolf.com>

- added man pages
- added bash,zsh,fish shell completions
- compile with optimization level 3, default for %{cargo_build}
- do not build with all features (vendor openssl, self-update)
- limit build number of CPUs to RPM variable

* Tue Mar 07 2025 Ernesto Martínez <me@ecomaikgolf.com>

- typst 0.13.1
- removed high CPU bug downstream patch as it got upstreamed

* Tue Mar 03 2025 Ernesto Martínez <me@ecomaikgolf.com>

- Patch PR 5905 which got merged but not released yet
- Removed no downstream patches rule as there's an important one

* Thu Feb 20 2025 Ernesto Martínez <me@ecomaikgolf.com>

- typst 0.13.0

* Mon Oct 21 2024 Ernesto Martínez <me@ecomaikgolf.com>

- Rollback rhel-based build support
- Undefine debug_package macro

* Mon Oct 21 2024 Ernesto Martínez <me@ecomaikgolf.com>

- Added rhel-based build support

* Mon Oct 21 2024 Ernesto Martínez <me@ecomaikgolf.com>
