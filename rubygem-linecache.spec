%define oname linecache

Name:       rubygem-%{oname}
Version:    0.43
Release:	3
Summary:    Read file with caching
Group:      Development/Ruby
License:    GPLv2+
URL:        http://rubyforge.org/projects/rocky-hacks/linecache
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
Requires:   ruby(abi) = 1.8
BuildRequires: rubygems
BuildRequires: ruby-devel
Provides:   rubygem(%{oname}) = %{version}

%description
LineCache is a module for reading and caching lines. This may be useful for
example in a debugger where the same lines are shown many times.


%prep
%setup -q
tar xmf data.tar.gz

%build
%gem_build

%install
%gem_install

#remove ext files
rm -rf %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/ext/

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
#%{ruby_gemdir}/gems/%{oname}-%{version}/test/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
#%doc %{ruby_gemdir}/gems/%{oname}-%{version}/AUTHORS
#%doc %{ruby_gemdir}/gems/%{oname}-%{version}/ChangeLog
#%doc %{ruby_gemdir}/gems/%{oname}-%{version}/COPYING
#%doc %{ruby_gemdir}/gems/%{oname}-%{version}/NEWS
#%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README
#%doc %{ruby_gemdir}/gems/%{oname}-%{version}/VERSION
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
%{ruby_sitearchdir}/trace_nums.so
