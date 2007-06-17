Summary:	ORM in the DataMapper pattern
Summary(pl.UTF-8):	ORM we wzorcu DataMapper
Name:		ruby-datamapper
Version:	0.0.20070608
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	datamapper-0.0.20070608.tar.gz
# Source0-md5:	2791245056d06c8036cef17b2057a6af
URL:		http://datamapper.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb = 3.3.1
Requires:	ruby-builder
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DataMapper is an Object-Relational mapper.

%description -l pl.UTF-8
DataMapper to mapper obiektowo-relacyjny.

%prep
%setup -q -n datamapper-%{version}
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/*
%{ruby_ridir}/DataMapper
