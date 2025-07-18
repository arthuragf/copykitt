import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lambda from 'aws-cdk-lib/aws-lambda'
import * as path from 'path';
import * as dotenv from 'dotenv';

// Carrega as variáveis do arquivo .env
dotenv.config({ path: path.resolve(__dirname, '../../app/.env') });

export class CopykittInfraStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    
    const layer = new lambda.LayerVersion(this, "BaseLayer", {
        code: lambda.Code.fromAsset("lambda_base_layer/layer.zip"),
        compatibleRuntimes: [lambda.Runtime.PYTHON_3_9]
    })
    
    const apiLambda = new lambda.Function(this, "ApiFunction", {
        runtime: lambda.Runtime.PYTHON_3_9,
        code: lambda.Code.fromAsset("../app/"),
        handler: "coppykit_api.handler",   
        layers: [layer],
        environment: {
            "GEMINI_API_KEY": process.env.GEMINI_API_KEY || 'FALHOU',   
        }
    })
  }
}
