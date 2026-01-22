const transformHook = (rw) => {
  // Access properties from UI controls
  const { heading } = rw.props;

  // Transform and pass data to templates
  rw.setProps({
    // Add processed values here
  });
};

exports.transformHook = transformHook;
