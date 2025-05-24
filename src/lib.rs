use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

#[pyfunction]
fn fib_rs(n: u64) -> u64 {
    match n {
        0 => 0,
        1 => 1,
        _ => fib_rs(n - 1) + fib_rs(n - 2),
    }
}

/// A Python module implemented in Rust.
#[pymodule]
fn python_rust_practice(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(fib_rs, m)?)?;
    Ok(())
}
