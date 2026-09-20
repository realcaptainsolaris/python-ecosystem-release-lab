# Python 3.15 Compatibility Results

Test results for selected Python ecosystem packages on CPython 3.15.0rc2.

## Test Platforms

| Platform                 | Architecture    | Python            |
| ------------------------ | --------------- | ----------------- |
| Kubuntu Linux            | x86_64          | CPython 3.15.0rc2 |
| Debian 13 (Raspberry Pi) | ARM64 / aarch64 | CPython 3.15.0rc2 |
| Windows 11               | x86_64          | CPython 3.15.0rc2 |

The Linux environments use uv-managed CPython builds.

The Windows tests use the official CPython 3.15.0rc2 distribution from python.org. The uv-managed Windows build could not load its OpenSSL `libcrypto-3-x64.dll` because of a local Windows Code Integrity policy. This is considered an environment-specific issue and not a Python 3.15 compatibility result.

## Method

Each package was checked for:

1. Installation under CPython 3.15
2. Availability of a compatible binary wheel
3. Successful import
4. Successful execution of a representative operation
5. Warnings or runtime errors

Wheel availability was tested with:

```bash
uv pip install --only-binary=:all: --reinstall PACKAGE
```

This prevents source builds and therefore exposes missing wheels for the current Python ABI, operating system and architecture.

## Results

| Package      | Version | Linux x86_64 | Linux ARM64 | Windows x86_64 |
| ------------ | ------: | ------------ | ----------- | -------------- |
| NumPy        |   2.5.3 | Pass         | Pass        | Pass           |
| pandas       |   3.0.6 | Pass         | Pass        | Pass           |
| Polars       |  1.44.2 | Pass         | Pass        | Pass           |
| SciPy        |  1.18.1 | Pass         | Pass        | Pass           |
| scikit-learn |   1.9.1 | Pass         | Pass        | Pass           |
| Matplotlib   |  3.11.2 | Pass         | Pass        | Pass           |
| Pydantic     |  2.13.5 | Pass*        | Pass*       | Build issue*   |
| PyArrow      |  25.0.1 | No wheel     | No wheel    | No wheel       |

The successful packages provided compatible CPython 3.15 wheels and passed their corresponding smoke tests without compatibility errors.

## Pydantic

Pydantic 2.13.5 depends on:

```text
pydantic-core==2.46.5
```

No usable CPython 3.15 wheel for this exact dependency version was available on any of the three tested platforms.

This was verified with:

```bash
uv pip install --only-binary=:all: --reinstall pydantic-core==2.46.5
```

On Linux x86_64 and ARM64, `pydantic-core` successfully compiled from source and the Pydantic smoke test subsequently passed.

On Windows x86_64, the source build required a Rust/MSVC build environment. Rust could be obtained automatically, but the build failed because the MSVC linker `link.exe` was not installed.

Therefore Pydantic itself worked where its native dependency could be built, but installation was not wheel-only on any tested platform.

## PyArrow

PyArrow 25.0.1 did not provide a usable CPython 3.15 wheel on any of the tested platforms.

The wheel-only installation failed on Linux x86_64, Linux ARM64 and Windows x86_64.

On Linux x86_64, a normal installation attempted to build PyArrow from source. CMake configuration then failed because the required Arrow C++ development libraries were not installed.

This does not prove that PyArrow cannot be built for Python 3.15. It shows that a fresh environment could not install it directly from an available binary wheel at the time of testing.

## Conclusion

CPython 3.15.0rc2 compatibility was already strong across the tested numerical and data-science stack.

NumPy, pandas, Polars, SciPy, scikit-learn and Matplotlib provided usable wheels and passed representative runtime tests on all three platforms.

The remaining friction was concentrated around native dependencies and wheel availability.

Pydantic worked but required `pydantic-core` to be compiled from source, while PyArrow did not yet provide a usable CPython 3.15 wheel on any of the tested platforms.

