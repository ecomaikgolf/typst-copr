Name:       typst
Version:    0.11.1
Release:    1
Summary:    A new markup-based typesetting system that is powerful and easy to learn.

License:    Apache-2.0
URL:        https://github.com/typst/typst
Source0:    %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: rust-packaging >= 21
BuildRequires: openssl 
BuildRequires: openssl-libs
BuildRequires: perl

%description
A new markup-based typesetting system that is powerful and easy to learn.

%prep
%autosetup

%build
cargo build -p typst-cli --release --all-features --locked

%install
install -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 target/release/typst %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
