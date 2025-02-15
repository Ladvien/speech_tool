:py:mod:`speech_neuron.config`
==============================

.. py:module:: speech_neuron.config

.. autodoc2-docstring:: speech_neuron.config
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`ResponseConfig <speech_neuron.config.ResponseConfig>`
     - .. autodoc2-docstring:: speech_neuron.config.ResponseConfig
          :summary:
   * - :py:obj:`PipelineConfig <speech_neuron.config.PipelineConfig>`
     - .. autodoc2-docstring:: speech_neuron.config.PipelineConfig
          :summary:
   * - :py:obj:`NodeConfig <speech_neuron.config.NodeConfig>`
     - .. autodoc2-docstring:: speech_neuron.config.NodeConfig
          :summary:

API
~~~

.. py:class:: ResponseConfig
   :canonical: speech_neuron.config.ResponseConfig

   .. autodoc2-docstring:: speech_neuron.config.ResponseConfig

   .. py:attribute:: type
      :canonical: speech_neuron.config.ResponseConfig.type
      :type: str
      :value: 'file'

      .. autodoc2-docstring:: speech_neuron.config.ResponseConfig.type

   .. py:attribute:: sample_rate
      :canonical: speech_neuron.config.ResponseConfig.sample_rate
      :type: int
      :value: 24000

      .. autodoc2-docstring:: speech_neuron.config.ResponseConfig.sample_rate

   .. py:attribute:: format
      :canonical: speech_neuron.config.ResponseConfig.format
      :type: str
      :value: 'wav'

      .. autodoc2-docstring:: speech_neuron.config.ResponseConfig.format

   .. py:attribute:: compression_level
      :canonical: speech_neuron.config.ResponseConfig.compression_level
      :type: int
      :value: 0

      .. autodoc2-docstring:: speech_neuron.config.ResponseConfig.compression_level

   .. py:method:: __post_init__()
      :canonical: speech_neuron.config.ResponseConfig.__post_init__

      .. autodoc2-docstring:: speech_neuron.config.ResponseConfig.__post_init__

.. py:class:: PipelineConfig
   :canonical: speech_neuron.config.PipelineConfig

   .. autodoc2-docstring:: speech_neuron.config.PipelineConfig

   .. py:attribute:: model
      :canonical: speech_neuron.config.PipelineConfig.model
      :type: typing.Optional[str]
      :value: None

      .. autodoc2-docstring:: speech_neuron.config.PipelineConfig.model

   .. py:attribute:: device
      :canonical: speech_neuron.config.PipelineConfig.device
      :type: str
      :value: 'cpu'

      .. autodoc2-docstring:: speech_neuron.config.PipelineConfig.device

   .. py:attribute:: use_transformer
      :canonical: speech_neuron.config.PipelineConfig.use_transformer
      :type: bool
      :value: False

      .. autodoc2-docstring:: speech_neuron.config.PipelineConfig.use_transformer

   .. py:attribute:: language_code
      :canonical: speech_neuron.config.PipelineConfig.language_code
      :type: str
      :value: 'b'

      .. autodoc2-docstring:: speech_neuron.config.PipelineConfig.language_code

   .. py:attribute:: speed
      :canonical: speech_neuron.config.PipelineConfig.speed
      :type: float
      :value: 1.0

      .. autodoc2-docstring:: speech_neuron.config.PipelineConfig.speed

   .. py:attribute:: voice
      :canonical: speech_neuron.config.PipelineConfig.voice
      :type: str
      :value: 'af_bella'

      .. autodoc2-docstring:: speech_neuron.config.PipelineConfig.voice

   .. py:attribute:: split_pattern
      :canonical: speech_neuron.config.PipelineConfig.split_pattern
      :type: str
      :value: '\\n+'

      .. autodoc2-docstring:: speech_neuron.config.PipelineConfig.split_pattern

   .. py:method:: __post_init__()
      :canonical: speech_neuron.config.PipelineConfig.__post_init__

      .. autodoc2-docstring:: speech_neuron.config.PipelineConfig.__post_init__

.. py:class:: NodeConfig
   :canonical: speech_neuron.config.NodeConfig

   .. autodoc2-docstring:: speech_neuron.config.NodeConfig

   .. py:attribute:: model_name
      :canonical: speech_neuron.config.NodeConfig.model_name
      :type: str
      :value: 'kokoro-v1.0.onnx'

      .. autodoc2-docstring:: speech_neuron.config.NodeConfig.model_name

   .. py:attribute:: voices_name
      :canonical: speech_neuron.config.NodeConfig.voices_name
      :type: str
      :value: 'voices-v1.0.bin'

      .. autodoc2-docstring:: speech_neuron.config.NodeConfig.voices_name

   .. py:attribute:: name
      :canonical: speech_neuron.config.NodeConfig.name
      :type: str
      :value: 'speech'

      .. autodoc2-docstring:: speech_neuron.config.NodeConfig.name

   .. py:attribute:: response
      :canonical: speech_neuron.config.NodeConfig.response
      :type: speech_neuron.config.ResponseConfig
      :value: None

      .. autodoc2-docstring:: speech_neuron.config.NodeConfig.response

   .. py:attribute:: pipeline
      :canonical: speech_neuron.config.NodeConfig.pipeline
      :type: speech_neuron.config.PipelineConfig
      :value: None

      .. autodoc2-docstring:: speech_neuron.config.NodeConfig.pipeline

   .. py:attribute:: base_download_link
      :canonical: speech_neuron.config.NodeConfig.base_download_link
      :value: 'https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0'

      .. autodoc2-docstring:: speech_neuron.config.NodeConfig.base_download_link

   .. py:attribute:: model_filenames
      :canonical: speech_neuron.config.NodeConfig.model_filenames
      :value: ['kokoro-v1.0.fp16-gpu.onnx', 'kokoro-v1.0.fp16.onnx', 'kokoro-v1.0.int8.onnx', 'kokoro-v1.0.onnx']

      .. autodoc2-docstring:: speech_neuron.config.NodeConfig.model_filenames

   .. py:attribute:: voices_filenames
      :canonical: speech_neuron.config.NodeConfig.voices_filenames
      :value: ['voices-v1.0.bin']

      .. autodoc2-docstring:: speech_neuron.config.NodeConfig.voices_filenames

   .. py:method:: __post_init__()
      :canonical: speech_neuron.config.NodeConfig.__post_init__

      .. autodoc2-docstring:: speech_neuron.config.NodeConfig.__post_init__
